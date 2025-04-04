// product-card/index.js
import { InnerPage} from "../inner-page/index.js";
import { ajax } from "../../modules/ajax.js";
import { urls } from "../../modules/urls.js";
export class ProductComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return `
                <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="${data.photo_400_orig}" class="img-fluid" alt="картинка">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data.first_name} ${data.last_name}</h5>
                                <p>ID: ${data.id}</p>
                                <p>Country: ${data.country}</p>
                                <p>Education: ${data.university_name}</p>
                                <p>Faculty: ${data.faculty_name}</p>
                                <button class="btn btn-primary click-card-btn" data-id="${data.id}">Перейти</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
    }
    getData() {
        ajax.post(urls.getUserInfo(this.data.id), (data) => {
            this.renderData(data.response);
        });
    }
    render(data) {
        this.data = data
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML("beforeend", html);
        this.addListeners();
    }
    
    renderData(item) {
        const innerPage = new InnerPage(document.body);
        innerPage.render(item[0]);
    }

    addListeners() {
        this.parent.querySelectorAll('.click-card-btn').forEach(button => {
            button.addEventListener("click", this.clickCard.bind(this));
        });
    }

    clickCard(e) {
        const cardId = e.target.dataset.id;
        console.log("pressed ", cardId);
        this.getData();
    }
}
