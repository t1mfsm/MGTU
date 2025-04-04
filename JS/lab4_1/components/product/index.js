export class ProductComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        let cityHTML = '';
        if (data.city) {
            cityHTML = `<h5 class="card-title">${data.city.title}</h5>`;
        } else {
            cityHTML = `<h5 class="card-title">Город не указан</h5>`;
        }
    
        return (
            `
            <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="${data.photo_200_orig}" class="img-fluid" alt="картинка">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data.first_name} ${data.last_name}</h5>
                            </div>
                        </div>
                    </div>
                </div>
            `
        )
    }
    
    
    // <h5 class="card-title">${data.bdate}</h5>
    // ${cityHTML}

    render(data) {
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML("beforeend", html);
    }
}