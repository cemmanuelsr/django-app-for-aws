from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def get_notes(request):
    try:
        notes = Note.objects.all()
    except Exception as e:
        return Response(str(e), status=HTTP_404_NOT_FOUND)

    return Response(NoteSerializer(notes, many=True).data)

@api_view(['GET'])
def get_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Exception as e:
        return Response(str(e), status=HTTP_404_NOT_FOUND)

    return Response(NoteSerializer(note).data)

@api_view(['POST'])
def create_note(request):
    note = Note(**request.data)
    note.save()

    return Response(NoteSerializer(note).data)

@api_view(['DELETE'])
def delete_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Exception as e:
        return Response(str(e), status=HTTP_404_NOT_FOUND)

    note.delete()
    return Response(status=HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_note(request, note_id):
    try:
        note = Note.objects.filter(id=note_id)
    except Exception as e:
        return Response(str(e), status=HTTP_404_NOT_FOUND)

    note.update(**request.data)

    return Response(NoteSerializer(note, many=True).data)
