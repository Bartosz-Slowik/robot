import telnetlib

class UEManagerClient:
    
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = telnetlib.Telnet(self.host, self.port)

    def close(self):
        if self.connection:
            self.connection.close()

    def attach_ue(self, cell, ue_id):
        command = f"attach ue={ue_id} cell={cell}"
        self._send_command(command)

    def detach_ue(self, cell, ue_id):
        command = f"detach ue={ue_id} cell={cell}"
        self._send_command(command)

    def start_traffic(self, ue_id):
        command = f"trf_data_start ue={ue_id}"
        self._send_command(command)

    def stop_traffic(self, ue_id):
        command = f"trf_data_stop ue={ue_id}"
        self._send_command(command)

    def verify_ue_attached(self, cell, ue_id):
        response = self._send_command(f"list_ue {cell}")
        
        return ue_id in response

    def _send_command(self, command):
        if not self.connection:
            raise Exception("Not connected to UE Manager application.")

        encoded_command = command.encode('utf-8')
        self.connection.write(encoded_command + b"\n")

        response = self.connection.read_until(b"\n").decode('utf-8')
        print(response)
        return response.strip()
    
def main():
    host = "pk-robot.ddns.net"
    port = 8000
    ue_manager = UEManagerClient(host, port)
    
    try:
        ue_manager.connect()
        cell=2
        ue_id = "420"
        ue_manager.attach_ue(cell, ue_id)
        
        if ue_manager.verify_ue_attached(cell, ue_id):
            print(f"UE {ue_id} is attached.")
        else:
            print(f"UE {ue_id} is not attached.")
        
        ue_manager.start_traffic(ue_id)
        
        # Do something with the UE
        
        ue_manager.stop_traffic(ue_id)
        
        ue_manager.detach_ue(ue_id, cell)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        ue_manager.close()

if __name__ == "__main__":
    main()