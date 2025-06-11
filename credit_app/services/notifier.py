"""Simple notifier via email or SMS."""

class Notifier:
    def notify_approval(self, correo: str, mensaje: str) -> None:
        print(f"Enviando aprobacion a {correo}: {mensaje}")

    def notify_rejection(self, correo: str, mensaje: str) -> None:
        print(f"Enviando rechazo a {correo}: {mensaje}")
