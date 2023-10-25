from telegram import Update
from telegram.ext import filters,ApplicationBuilder,ContextTypes,CommandHandler,MessageHandler

class Bot:
    def __init__(self,token:str,id:str) -> None:
        self.id=id
        self.app=ApplicationBuilder().token(token).build()
    
    #def __post_init__(self):

    def start(self):
        self.app.add_handler(CommandHandler("test",self.reply))
        self.app.add_handler(CommandHandler("id",self.id))
        self.app.add_handler(CommandHandler("id",self.id))
        self.app.add_handler(MessageHandler(filters.ALL,self.get_correct_post))
        print("starting")
        self.app.run_polling()
        
    @staticmethod
    async def id(update:Update,context:ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message("-1001909202660",update.effective_chat.id)
        
    @staticmethod
    async def reply(update:Update,context:ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message("barbamento","ciao")
        
    @staticmethod
    async def get_correct_post(update:Update,context:ContextTypes.DEFAULT_TYPE):
        print(update)
        #await context.bot.send_message("-1001909202660",update)
        