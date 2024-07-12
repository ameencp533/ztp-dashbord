from flask import render_template, jsonify, request,Blueprint
from . import db
from .models import Device
from datetime import datetime
from .netconf_handler import start_netconf_session

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    devices = Device.query.all()
    return render_template('index.html', devices=devices)

@bp.route('/device-status', methods=['POST'])
def device_status():
    data = request.json
    ip_address = data['ip_address']
    status = data['status']
    
    device = Device.query.filter_by(ip_address=ip_address).first()
    if not device:
        device = Device(ip_address=ip_address, status=status, last_updated=datetime.utcnow())
    else:
        device.status = status
        device.last_updated = datetime.utcnow()
    
    db.session.add(device)
    db.session.commit()
    
    if status == 'ready for SSH and NETCONF':
        start_netconf_session(ip_address, 'your-username', 'your-password')
    
    return jsonify({'message': 'Device status updated successfully'}), 200