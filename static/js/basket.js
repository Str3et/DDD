let config = {
    selectors: {
        add: '.basket-item-add',
        del: '.basket-item-del',
        quantity: '.basket-item-quantity',
    },
    urls: {
        add: '/basket/add/',
        update: '/basket/update/',
        del: '/basket/remove/',
    }
};

$(document).ready(function () {
    $(config.selectors.add).on('click', function(){
        let item_id = $(this).data('id');
        let item_url = config.urls.add + item_id;
        let parent_item = $(this).parents()[0];
        let counter = $(parent_item).find(config.selectors.quantity);

        // let test = document.getElementById('my-shop');
        // console.log(test);

        $.ajax({
            url: item_url,
            success: function (data) {
                counter.text(data.quantity);
            },
        })
    })
});
