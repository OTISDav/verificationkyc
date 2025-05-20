from deepface import DeepFace

def compare_faces(id_image_path, selfie_path, model_name="Facenet", distance_threshold=1.10):
    try:
        result = DeepFace.verify(
            img1_path=id_image_path,
            img2_path=selfie_path,
            model_name=model_name,
            enforce_detection=False
        )

        distance = result["distance"]
        verified = distance <= distance_threshold

        return verified, distance

    except Exception as e:
        print(f"Erreur lors de la comparaison : {e}")
        return False, 100.0
