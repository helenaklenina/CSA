import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Client {
    public static void main(String[] args) throws IOException {
        try {
            Socket soc = new Socket("localhost", 1234);
            DataOutputStream outC = new DataOutputStream(soc.getOutputStream());
            DataInputStream inC = new DataInputStream(soc.getInputStream());
            System.out.print("Client connect to soc\n");
            System.out.println("Client writing channel = outC & reading channel = inC initialized.");
            outC.writeUTF("hello"); //запись данных с консоли в канал сокета для сервера
            System.out.println("Client sent message to server");
            String str = inC.readUTF();
            System.out.println( "Message from cserver - "+ str);

            inC.close();
            outC.close();
            soc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
