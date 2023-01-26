from flask import Flask, jsonify, request
from flask_cors import CORS
from os import environ
from config import db, SECRET_KEY
from dotenv import load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.projects import Projects
from models.experiences import Experiences
from models.education import Education
from models.certificates import Certificates
from models.skills import Skills


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        """
        Create an endpoint

        use form data to take the response from the user
        use username for indexing a user
            - sign up suers
            - add personal details
            - add experiences details
            - add projects details
            - add education details
            - add certificate details
            - add skills details
        """
        @app.route("/sign_up", methods=["POST"])
        def sign_up():
            data = request.form.to_dict(flat=True)
            new_user = User(
                username = data["username"]
            )
            db.session.add(new_user)
            db.session.commit()

            return "User added successfully"

        @app.route("/add_personal_details", methods=["POST"])
        def add_personal_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            """
            {
                "name": "",
                "email": "",
                "phone": "",
                "address": "",
                "linkedin_link": ""
            }
            """
            personal_details = request.get_json()
            new_personal_details = PersonalDetails(
                name = personal_details["name"],
                email = personal_details["email"],
                phone = personal_details["phone"],
                address = personal_details["address"],
                linkedin_link = personal_details["linkedin_link"],
                user_id = user.id
            )
            db.session.add(new_personal_details)
            db.session.commit()

            return "Personal Details added successfully"

        @app.route("/add_experiences_details", methods=["POST"])
        def add_experiences_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            experiences_data = request.get_json()
            print(experiences_data)
            for experience in experiences_data["data"]:
                new_experience = Experiences(
                    company_name = experience["company_name"],
                    role = experience["role"],
                    role_desc = experience["role_desc"],
                    start_date = experience["start_date"],
                    end_date = experience["end_date"],
                    user_id = user.id
                )
                db.session.add(new_experience)
            db.session.commit()

            return jsonify(msg="Experiences Added Successfully")
   

        @app.route("/add_projects_details", methods=["POST"])
        def add_projects_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            project_data = request.get_json()  
            print(project_data)
            for project in project_data["data"]:
                new_project = Projects(
                    name = project["name"],
                    desc = project["description"],
                    start_date = project["start_date"],
                    end_date = project["end_date"],
                    user_id = user.id
                )
                db.session.add(new_project)
            db.session.commit()

            return jsonify(msg="Project Added Successfully")

        @app.route("/add_education_details", methods=["POST"])
        def add_education_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            education_details = request.get_json()

        @app.route("/add_certificate_details", methods=["POST"])
        def add_certificate_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            certificate_details = request.get_json()   

        @app.route("/add_skills_details", methods=["POST"])
        def add_skills_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            skills_details = request.get_json()     

        @app.route("/get_resume", methods=["GET"])
        def get_resume():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            personal_details = PersonalDetails.query.filter_by(user_id=user.id).first()
            experiences = Experiences.query.filter_by(user_id=user.id).all()
            education = Education.query.filter_by(user_id=user.id).all()
            projects = Projects.query.filter_by(user_id=user.id).all()
            certificates = Certificates.query.filter_by(user_id=user.id).all()
            skills = Skills.query.filter_by(user_id=user.id).all()


            experiences_data = [] 
            education_data = [] 
            projects_data = [] 
            certificates_data = [] 
            skills_data = [] 

            resume_data = {
                "name": personal_details.name,
                "email": personal_details.email,
                "phone": personal_details.phone,
                "address": personal_details.address,
                "linkedin_link": personal_details.linkedin_link
            }

            # add experience
            for exp in experiences:
                experiences_data.append(
                    {
                        "company_name": exp.company_name,
                        "role": exp.role,
                        "role_desc": exp.role_desc,
                        "start_date": exp.start_date,
                        "end_date": exp.end_date
                    }
                )
            resume_data["experiences"] = experiences_data

            # add projects
            # for proj in projects:
            #     projects_data.append(
            #         {
            #             "name": proj.name,
            #             "desc": proj.role,
            #             "start_date": proj.start_date,
            #             "end_date": proj.end_date
            #         }
            #     )    
            # resume_data["projects"] = projects_data

            return resume_data
                   
        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
