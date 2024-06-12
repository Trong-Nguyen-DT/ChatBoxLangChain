from fastapi import APIRouter
from app.schemas.response import Response
from app.schemas.request import Request
from app.models import ConversationAzureChatGPT35TURBO16K

router = APIRouter()

@router.post("/chat_completion", response_model=Response)
async def chat_completion(request: Request) -> Response:
    chat = ConversationAzureChatGPT35TURBO16K()
    data = chat.run(request.question)['output']
    return Response(status=200, message="success", data=data)