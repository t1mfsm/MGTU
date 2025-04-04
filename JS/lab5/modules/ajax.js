

class Ajax {
    post(url, callback) {
        console.log(url)
        let xhr = new XMLHttpRequest()
        xhr.open('POST', url, true)
        xhr.send()

        xhr.onreadystatechange = () => {
            if(xhr.readyState == 4 && xhr.status == 200) {
                const data = JSON.parse(xhr.response)
                //console.log(data)
                callback(data)
            }
        }
    }
}

export const ajax = new Ajax();