import axios from "axios";

export function RequestInfo(url, method, request_data) {
    if (method.toLowerCase() === "get") {
        return axios.get(url)
            .then((response) => {
                return response.data;
            })
            .catch(function (error) {
                console.log('ERROR!! ' + error);
                return 'ERROR!!'
            })
            .finally(function () {
                // 总是会执行
                console.log('finally');
            }); 
    }else if (method.toLowerCase() === "post") {
        return axios.post(url, request_data)
           .then((response) => {
                return response.data;
            })
           .catch(function (error) {
                console.log('ERROR!! ' + error);
                return 'ERROR!!'
            })
           .finally(function () {
                // 总是会执行
                console.log('finally');
            });
    }
    else{
        console.log("method error");
    }
}