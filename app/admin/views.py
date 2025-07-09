from flask import Blueprint, render_template, jsonify

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def dashboard():
    return 'Дашборд (заглушка)'

@admin_bp.route('/accounts')
def accounts():
    return 'Telegram-аккаунты (заглушка)'

@admin_bp.route('/channels')
def channels():
    return 'Каналы и посты (заглушка)'

@admin_bp.route('/comments')
def comments():
    return 'Генерация комментариев (заглушка)'

@admin_bp.route('/inbox')
def inbox():
    return 'Входящие (заглушка)'

@admin_bp.route('/groups')
def groups():
    return 'Обучающие группы (заглушка)'

@admin_bp.route('/scripts')
def scripts():
    return 'Скрипты (заглушка)'

@admin_bp.route('/logs')
def logs():
    return 'Логи и история (заглушка)'

@admin_bp.route('/users')
def users():
    return 'Пользователи и доступ (заглушка)'

@admin_bp.route('/settings')
def settings():
    return 'Системные параметры (заглушка)' 