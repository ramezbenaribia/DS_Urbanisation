from fastapi import APIRouter , Response



router = APIRouter()

days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday", "Sunday"]


# insert data
@router.get('/day_of_week')
async def store(num:int):
    if num <= len(days) and num > 0 :
        response = days[num-1]
        response_content = """
        <response>
            <content>
           """ + response + """        
            </content>
        </response>
        """
    else:
        response_content = """
        <error>
            <content>
            error
        
            </content>
        </error>
        """
    return Response(content=response_content, media_type="application/xml")


  
