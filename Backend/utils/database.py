from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGODB_URL
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL)["MediConnect"]
logger.info("Connected to MongoDB")

AUTHDB = DB["AUTHDB"]
SHOPDB = DB["SHOPDB"]

# Auth Functions

# Auth Data {"email": str, "password": str}


async def new_auth(email: str, password: str) -> bool:
    auth = await AUTHDB.find_one({"email": email})
    if auth:
        return False, "Email is already registered, please login"

    await AUTHDB.insert_one({"email": email, "password": password})
    return True, "Account Created Successfully"


async def check_auth(email: str, password: str) -> bool:
    auth = await AUTHDB.find_one({"email": email})
    if auth:
        if auth["password"] == password:
            return True, "Login Successful"
        else:
            return False, "Invalid Password"
    else:
        return False, "Invalid Email"


# Shop Functions

# Shop Data {"email": str, "shop_name": str, "shop_address": str, "shop_phone": str}


async def update_shop(email, data):
    await SHOPDB.update_one({"email": email}, {"$set": data}, upsert=True)


async def get_shop(email: str):
    shop_data = await SHOPDB.find_one({"email": email})
    return True, shop_data
