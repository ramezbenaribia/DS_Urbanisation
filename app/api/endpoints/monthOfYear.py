from fastapi import APIRouter , Response



router = APIRouter()

month = ["January", "February", "March", "April", "May", "June", "July",  "August", "September", "October", "November", "December"]


# insert data
@router.get('/month_of_year')
async def store(num:int):
    if num <= len(month) and num > 0 :
        response = month[num-1]
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


  
