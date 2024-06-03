from flask import jsonify
from src.models import SessionLocal, User, Ticket, UsersGroup, Role

from flask_login import login_user
from flask_login import LoginManager

login_manager = LoginManager() 


@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as session:
        return session.query(User).get(user_id)
    


class CreateUser():
    @staticmethod
    def create(data: dict):
        with SessionLocal() as session:
            obj = User(**data)
            session.add(obj)
            session.commit()
            return {"message": "The user was registered"}



class LoginUser():
    @staticmethod
    def login(username, password):
        with SessionLocal() as session:
            user = session.query(User).filter_by(username=username, password=password).first()
            if user:
                role_name = user.role.name
                login_user(user, remember=True)
                return jsonify({"message": "Hi! You are loggen in", "role_name": role_name}), 200
            else:
                return jsonify({"message": "Access denied"}), 403
            


class AuthUser():
    @staticmethod
    def authentication(username, password):
        with SessionLocal() as session:  
            user = session.query(User).filter_by(username=username, password=password).first()
            if user:
                role_name = user.role.name

                groups = session.query(UsersGroup).filter_by(id=user.group_id).first()
                tickets = session.query(Ticket).filter_by(group_id=user.group_id).all()

                ticket_data = [{"id": ticket.id, "status": str(ticket.status), "note": str(ticket.note)} for ticket in tickets]

                login_user(user, remember=True)
                return jsonify({
                "message": f"Hi, {role_name}! Your Group: {groups.username}. Your Tickets: {ticket_data}"}), 200









                




                
                


            


            
                    
