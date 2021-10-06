from wasap.wasap import Wasap


def main():
    with Wasap() as wa:
        running = True
        while running:
            inputs = input("wasap:").split(" ")
            command = inputs[0]
            args = inputs[1:]
            if not command:
                continue
            elif command == "chat":
                if not args:
                    print("No contact name argument provided.")
                elif len(args) > 1:
                    print("Too many arguments provided.")
                else:
                    try:
                        wa.select_chat(args[0])
                    except:
                        print("Error selecting chat.")
            elif command == "message":
                if not args:
                    print("No message argument provided.")
                else:
                    try:
                        wa.send_message(" ".join(args))
                    except:
                        print("Error sending message.")
            elif command == "quit":
                running = False
                continue
            else:
                print("Unknown command.")
