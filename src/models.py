from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()


def db_connect(uri):
    engine = create_engine(uri)
    SessionLocal.configure(bind=engine)


def db_disconnect():
    if SessionLocal.kw is not None and SessionLocal.kw.get("bind") is not None:
        SessionLocal.kw["bind"].dispose()



class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("Role.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("UsersGroup.id"), nullable=False) 

    role = relationship("Role", back_populates="users")
    group = relationship("UsersGroup")

    def get_id(self):
        return str(self.id)



class Role(Base):
    __tablename__ = "Role"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    users = relationship("User", back_populates="role")



class UsersGroup(Base):
    __tablename__ = "UsersGroup"

    id = Column(Integer,primary_key=True, index=True )
    username = Column(String(50), nullable=False)

    tickets = relationship("Ticket", back_populates="groups")



class Ticket(Base):
    __tablename__ = "Ticket"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(200), nullable=False)
    note = Column(String(250))
    group_id = Column(Integer, ForeignKey("UsersGroup.id"), nullable=False)

    groups = relationship("UsersGroup", back_populates="tickets")




