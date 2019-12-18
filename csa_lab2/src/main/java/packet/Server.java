package packet;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serever = new ServerSocket(1234);
        while(true) {
            Socket client = serever.accept();
            System.out.println("Connect");
            DataInputStream in = new DataInputStream(client.getInputStream());//чтение из сокета
            System.out.println("input create");
            DataOutputStream out = new DataOutputStream(client.getOutputStream());//запись в сокет
            System.out.println("output create");
            String mes = in.readUTF(); // получение данных
            System.out.println("read from mes -" + mes);
            out.writeUTF(mes + "!!!"); // Отправка ответа
            System.out.println("Write the answer to client -" + mes);

            in.close();
            out.close();
            client.close();
        }

    }

}
