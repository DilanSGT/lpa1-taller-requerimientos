# app/routes/reservas.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Reserva, Cliente, Habitacion, EstadoReserva, TransaccionPago, TipoPago, EstadoPago
from app.extensions import db
from datetime import datetime, date

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route('/')
def listar():
    """Lista todas las reservas."""
    reservas = Reserva.query.join(Cliente).join(Habitacion).all()
    return render_template('reservas/listar.html', reservas=reservas)

@reservas_bp.route('/crear/<habitacion_id>', methods=['GET', 'POST'])
def crear(habitacion_id):
    """Crear una nueva reserva para una habitación."""
    habitacion = Habitacion.query.get_or_404(habitacion_id)
    clientes = Cliente.query.all()
    
    if request.method == 'POST':
        try:
            fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
            
            # Validaciones básicas
            if fecha_inicio >= fecha_fin:
                flash('La fecha de fin debe ser posterior a la fecha de inicio', 'error')
                return render_template('reservas/crear.html', habitacion=habitacion, clientes=clientes)
            
            if fecha_inicio < date.today():
                flash('No se pueden hacer reservas para fechas pasadas', 'error')
                return render_template('reservas/crear.html', habitacion=habitacion, clientes=clientes)
            
            cantidad_personas = int(request.form['cantidad_personas'])
            if cantidad_personas > habitacion.capacidad:
                flash(f'La habitación solo tiene capacidad para {habitacion.capacidad} personas', 'error')
                return render_template('reservas/crear.html', habitacion=habitacion, clientes=clientes)
            
            # Calcular total (precio base * días)
            dias = (fecha_fin - fecha_inicio).days
            total = float(habitacion.precio_base) * dias
            
            # Crear la reserva
            reserva = Reserva(
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                cantidad_personas=cantidad_personas,
                total=total,
                estado=EstadoReserva.PENDIENTE,
                cliente_id=request.form['cliente_id'],
                habitacion_id=habitacion.id
            )
            
            db.session.add(reserva)
            db.session.flush()  # Para obtener el ID
            
            # Crear transacción de pago
            transaccion = TransaccionPago(
                tipo=TipoPago(request.form.get('tipo_pago', 'tarjeta')),
                monto=total,
                estado=EstadoPago.PENDIENTE,
                reserva_id=reserva.id
            )
            
            db.session.add(transaccion)
            db.session.commit()
            
            flash('Reserva creada exitosamente', 'success')
            return redirect(url_for('reservas.detalle', reserva_id=reserva.id))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear reserva: {str(e)}', 'error')
    
    return render_template('reservas/crear.html', 
                         habitacion=habitacion, 
                         clientes=clientes,
                         tipos_pago=TipoPago)

@reservas_bp.route('/<reserva_id>')
def detalle(reserva_id):
    """Detalle de una reserva específica."""
    reserva = Reserva.query.get_or_404(reserva_id)
    return render_template('reservas/detalle.html', reserva=reserva)

@reservas_bp.route('/<reserva_id>/confirmar', methods=['POST'])
def confirmar_pago(reserva_id):
    """Confirmar el pago de una reserva."""
    reserva = Reserva.query.get_or_404(reserva_id)
    
    try:
        # Cambiar estado de la reserva
        reserva.estado = EstadoReserva.CONFIRMADA
        
        # Cambiar estado del pago
        if reserva.transaccion_pago:
            reserva.transaccion_pago.estado = EstadoPago.AUTORIZADO
        
        db.session.commit()
        flash('Pago confirmado y reserva actualizada', 'success')
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al confirmar pago: {str(e)}', 'error')
    
    return redirect(url_for('reservas.detalle', reserva_id=reserva.id))

@reservas_bp.route('/<reserva_id>/cancelar', methods=['POST'])
def cancelar(reserva_id):
    """Cancelar una reserva."""
    reserva = Reserva.query.get_or_404(reserva_id)
    
    try:
        reserva.estado = EstadoReserva.CANCELADA
        
        # Si había pago, marcarlo como reembolsado
        if reserva.transaccion_pago and reserva.transaccion_pago.estado == EstadoPago.AUTORIZADO:
            reserva.transaccion_pago.estado = EstadoPago.REEMBOLSADO
        
        db.session.commit()
        flash('Reserva cancelada exitosamente', 'success')
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al cancelar reserva: {str(e)}', 'error')
    
    return redirect(url_for('reservas.detalle', reserva_id=reserva.id))

@reservas_bp.route('/<reserva_id>/completar', methods=['POST'])
def completar(reserva_id):
    """Marcar una reserva como completada."""
    reserva = Reserva.query.get_or_404(reserva_id)
    
    try:
        reserva.estado = EstadoReserva.COMPLETADA
        db.session.commit()
        flash('Reserva marcada como completada', 'success')
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al completar reserva: {str(e)}', 'error')
    
    return redirect(url_for('reservas.detalle', reserva_id=reserva.id))
