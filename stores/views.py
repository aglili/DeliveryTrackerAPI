from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework import status
from .serializer import CreateStoreSerializer,StoreSerializer
from accounts.permissions import IsRegionalManager,IsPresident,IsRegionalManagerOrPresident
from rest_framework.permissions import IsAuthenticated
from .models import Store



@api_view(["POST"])
@permission_classes([IsAuthenticated,IsRegionalManagerOrPresident])
def createStore(request):
    try:
        serializer = CreateStoreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status":"True",
                "message":"Store Created",
                "data":serializer.data,
            },status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            "status": "False",
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsRegionalManagerOrPresident])
def deleteStore(request,store_id:str):
    try:
        store = Store.objects.get(store_id=store_id)
        store.delete()
        return Response({
            "status":"True",
            "message":"Store Has Been Deleted"
        },status=status.HTTP_200_OK)
    except Store.DoesNotExist:
         return Response(
            {
                "status": "False",
                "message": "Store Does Not Exist"
            },status=status.HTTP_404_NOT_FOUND
         )
    except Exception as e:
        return Response({
            "status": "False",
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
            
    





@api_view(["GET"])
@permission_classes([IsAuthenticated,IsRegionalManagerOrPresident])
def getStore(request, store_id:str):
    try:
        store = Store.objects.get(store_id=store_id)
        serializer = StoreSerializer(store)
        print(serializer.data)
        return Response({
            "status": "True",
            "store_data": serializer.data
        })
    except Store.DoesNotExist:
        return Response(
            {
                "status": "False",
                "message": "Store Does Not Exist"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({
            "status": "False",
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
            

    


        
