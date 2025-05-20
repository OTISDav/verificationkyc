from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import tempfile

from .kyc_utils.text_utils import normalize_text
from .serializers import KYCSerializer
from .kyc_utils.ocr import extract_text_from_image
from .kyc_utils.face_match import compare_faces

class KYCVerificationView(APIView):
    def post(self, request):
        serializer = KYCSerializer(data=request.data)
        if serializer.is_valid():
            id_doc = serializer.validated_data['id_document']
            selfie = serializer.validated_data['selfie']
            id_number_input = serializer.validated_data['id_number_input']

            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_id, \
                 tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_selfie:

                temp_id.write(id_doc.read())
                temp_selfie.write(selfie.read())
                temp_id.flush()
                temp_selfie.flush()


                extracted_text = extract_text_from_image(temp_id.name)
                # print("Texte extrait :\n", extracted_text)


                id_input_norm = normalize_text(id_number_input)
                ocr_text_norm = normalize_text(extracted_text)

                id_match = id_input_norm in ocr_text_norm

                face_match, score = compare_faces(temp_id.name, temp_selfie.name)

                return Response({
                    # "ocr_result": extracted_text,
                    "id_number_match": id_match,
                    "face_match": face_match,
                    "face_score": round(score, 2),
                    "verified": face_match and id_match
                })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
