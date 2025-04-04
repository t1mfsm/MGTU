class Ajax {
    post(url, callback) {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    const data = JSON.parse(xhr.responseText);
                    callback(data);
                } else {
                    console.error(`Error: ${xhr.status} ${xhr.statusText}`);
                }
            }
        };
        xhr.send();
    }
}

export const ajax = new Ajax();
