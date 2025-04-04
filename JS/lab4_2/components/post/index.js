export class PostComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(post) {
        return `
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">Пост #${post.id}</h5>
                    <p class="card-text">${post.text}</p>
                </div>
            </div>
        `;
    }

    render(post) {
        const html = this.getHTML(post);
        this.parent.insertAdjacentHTML('beforeend', html);
    }
}
