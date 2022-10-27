def make_nats(project_name: str) -> None:
    """
    Make nats.

    :param project_name: project name in string type (e.g. my_project)
    """

    with open(f"{project_name}/internals/nats/nats.py", "w") as nats:
        nats.write("from typing import List\n")
        nats.write("from internals.log import logger\n")
        nats.write("from config import config\n")
        nats.write("from .subscribe import subscribe_on_foo\n\n")
        nats.write("import nats\n\n")

        nats.write("nats_subscribes: List[nats.Subscription] = []\n\n\n")

        nats.write("async def subscribe_all_topics() -> None:\n")
        nats.write("    await subscribe_on_foo.subscribe()\n\n\n")

        nats.write("async def unsubscribe_all_subscribers() -> None:\n")
        nats.write("    for sub in nats_subscribes:\n")
        nats.write("        await sub.unsubscribe()\n\n\n")

        nats.write("async def create_client() -> nats.Nats:\n")
        nats.write("    nc = await nats.connect(\n")
        nats.write("        servers=config.nats.address,\n")
        nats.write("        name=config.nats.name,\n")
        nats.write("        username=config.nats.username,\n")
        nats.write("        password=config.nats.password,\n")
        nats.write("        drain_timeout=config.nats.drain_timeout,\n")
        nats.write("        flush_timeout=config.nats.flush_timeout,\n")
        nats.write("        connect_timeout=config.nats.connect_timeout,\n")
        nats.write("        reconnect_time_wait=config.nats.reconnect_time_wait,\n")
        nats.write("        error_cb=nats_error_callback,\n")
        nats.write("        disconnected_cb=nats_disconnected_callback,\n")
        nats.write("        closed_cb=nats_closed_callback,\n")
        nats.write("        reconnected_cb=nats_reconnected_callback,\n")
        nats.write("    )\n")
        nats.write("    return nc\n\n\n")

        nats.write("async def nats_error_callback() -> None:\n")
        nats.write("    logger.error('error in nats')\n\n\n")

        nats.write("async def nats_disconnected_callback() -> None:\n")
        nats.write("    logger.warning('disconnected from Nats')\n\n\n")

        nats.write("async def nats_closed_callback() -> None:\n")
        nats.write("    logger.warning('Nats connection closed')\n\n\n")

        nats.write("async def nats_reconnected_callback() -> None:\n")
        nats.write("    logger.warning('Nats connection is reconnected')\n\n\n")

        nats.write("async def default_message_handler(msg) -> None:\n")
        nats.write("    subject = msg.subject\n")
        nats.write("    reply = msg.reply\n")
        nats.write("    data = msg.data.decode()\n")
        nats.write("    print(\"Received a message on '{subject} {reply}': {data}\".format(\n")
        nats.write("        subject=subject, reply=reply, data=data))\n")

    with open(f"{project_name}/internals/nats/__init__.py", "w") as init:
        init.write(
            "from .nats import create_client, default_message_handler, subscribe_all_topics, unsubscribe_all_subscribers\n"
        )
