def make_nats(project_name: str) -> None:
    """
    make nats example.

    :param project_name: project name
    """

    with open(f"{project_name}/internals/nats/publish.py", "w") as pub:
        pub.write("from internals.app import app\n\n\n")

        pub.write("async def publish_on_foo(data: bytes) -> None:\n")
        pub.write("    await app.nats_client.publish(\"foo\", data)\n")

    with open(f"{project_name}/internals/nats/subscribe.py", "w") as sub:
        sub.write("from .nats import default_message_handler, nats_subscribes\n")
        sub.write("from internals.app import app\n\n")
        sub.write("import nats\n\n\n")

        sub.write("async def subscribe_on_foo(message_handler=default_message_handler) -> nats.Subscription:\n")
        sub.write("    sub = await app.nats_client.subscribe(\"foo\", cb=message_handler)\n")
        sub.write("    nats_subscribes.append(sub)\n")
        sub.write("    return sub\n")
