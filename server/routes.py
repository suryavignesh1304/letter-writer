from flask import request, jsonify
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import time
from models import db, Draft

def init_routes(app):
    def get_drive_service(token):
        creds = Credentials(token=token)
        return build("drive", "v3", credentials=creds)

    @app.route("/save", methods=["POST"])
    def save_letter():
        user = request.user
        content = request.json.get("content")
        if not content:
            return jsonify({"error": "No content provided"}), 400

        # Save draft to PostgreSQL
        draft = Draft(user_id=user["uid"], content=content)
        db.session.add(draft)
        db.session.commit()

        # Save to Google Drive
        token = request.headers.get("Authorization").split("Bearer ")[1]
        drive_service = get_drive_service(token)

        file_metadata = {
            "name": f"Letter_{user['uid']}_{int(time.time())}.doc",
            "mimeType": "application/vnd.google-apps.document",
        }
        file = drive_service.files().create(body=file_metadata).execute()
        drive_service.files().update(
            fileId=file["id"],
            media_body=content,
            media_mime_type="text/plain",
        ).execute()

        return jsonify({"message": "Letter saved", "fileId": file["id"]})