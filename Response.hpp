#include <string>
#include <vector>
#include <map>

class Response
{
private:
    std::string version; //http버전
    std::string status; //상태코드 (ex "505").
    std::string status_msg; //상태코드 해석 메세지.
    std::map<std::string,std::string> header_map; //헤더필드의 키=값.
    std::string body; //바디.

public
    Response(/* args */);
    ~Response();

    std::string getVersion()
    {
        return this.version;
    }

public
    void setVersion(std::string version)
    {
        this.version = version;
    }

public
    std::string getStatus()
    {
        return this.status;
    }

public
    void setStatus(std::string status)
    {
        this.status = status;
    }

public
    std::string getStatus_msg()
    {
        return this.status_msg;
    }

public
    void setStatus_msg(std::string status_msg)
    {
        this.status_msg = status_msg;
    }

public
    std::map<std::string, std::string> getHeader_map()
    {
        return this.header_map;
    }

public
    void setHeader_map(std::map<std::string, std::string> header_map)
    {
        this.header_map = header_map;
    }

public
    std::string getBody()
    {
        return this.body;
    }

public
    void setBody(std::string body)
    {
        this.body = body;
    }

    //응답클래스의 멤버변수를 조합하여 최종 전송 할 데이터를 만드는 메소드
    std::string make_send_data();
    {
        std::string send_data;

        //정보를 조합해서 send_data를 만들어 반환. 
        return send_data;
    }

};

