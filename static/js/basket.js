let config = {
    selectors: {
        add: '.basket-item-add',
        del: '.basket-item-del',
        quantity: '.basket-item-quantity',
        total_quantity: '#my-shop',
        total_cost: '#my-shop-total-cost',
        item_total_cost: '.my-shop-item-total-cost',
    },
    urls: {
        add: '/basket/add/',
        update: '/basket/update/',
        delete: '/basket/delete/',
    }
};

$(document).ready(function () { // анонимная функция загруженная на страницу
    $(config.selectors.add).on('click', function(){  //  вешаем слушателя клика на селектор адд
        let item_id = $(this).data('id');    //  специальная метка data-id
        let item_url = config.urls.add + item_id;   //  формируем правильный адрес для похода в адд
        let parent_item = $(this).parents()[0];   //  вызываем все родительские блоки и берем нужный нам, нулевой.
        let total_counter = $(document).find(config.selectors.total_quantity);
        let total_cost = $(document).find(config.selectors.total_cost);
        let counter = $(parent_item).find(config.selectors.quantity);  // в родительском блоке достаём именно там где число для изменения.
        let paren_item_total_item_cost = $(this).parents()[1];
        let total_item_cost = $(paren_item_total_item_cost).find(config.selectors.item_total_cost);
        // console.log();

        $.ajax({  // включаем аякс запрос
            url: item_url, // говорим куда надо пойти аяксу после выполнения клика, метод адд в вьюхе баскета.
            success: function (data) {  //  если всё хорошо исполняем эту функцию. В дата мы получаем результат адд json.
                counter.text(data.quantity);  //  указываем найденное место и текст, который хотим вставить.
                total_counter.text(data.total_quantity);
                total_cost.text(data.total_cost);
                total_item_cost.text(data.quantity * data.price);
            },
        })
    })
});

$(document).ready(function () { // анонимная функция загруженная на страницу
    $(config.selectors.del).on('click', function(){  //  вешаем слушателя клика на селектор delete
        let item_id = $(this).data('id');    //  специальная метка data-id
        let item_url = config.urls.delete + item_id;   //  формируем правильный адрес для похода в del
        let parent_item = $(this).parents()[0];   //  вызываем все родительские блоки и берем нужный нам, нулевой.
        let total_counter = $(document).find(config.selectors.total_quantity);
        let total_cost = $(document).find(config.selectors.total_cost);
        let counter = $(parent_item).find(config.selectors.quantity);  // в родительском блоке достаём именно там где число для изменения.

        let paren_item_quantity_null = $(this).parents()[0];
        let quantity_null = $(paren_item_quantity_null).find(config.selectors.del);

        let paren_item_total_item_cost = $(this).parents()[1];
        let total_item_cost = $(paren_item_total_item_cost).find(config.selectors.item_total_cost);
        console.log(quantity_null);
        $.ajax({  // включаем аякс запрос
            url: item_url, // говорим куда надо пойти аяксу после выполнения клика, метод адд в вьюхе баскета.
            success: function (data) {  //  если всё хорошо исполняем эту функцию. В дата мы получаем результат адд json.
                counter.text(data.quantity);  //  указываем найденное место и текст, который хотим вставить.
                total_counter.text(data.total_quantity);
                total_cost.text(data.total_cost);
                total_item_cost.text(data.quantity * data.price);
                if (data.quantity === 0) {
                    quantity_null.hide()
                };
            },
        })
    })
});
