from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)



    def book_string(self):
        return f"{self.id} : {self.title} Descriptions: {self.description}"