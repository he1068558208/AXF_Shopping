

function addCart(goods_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/axf/addCart/',
        type:'POST',
        data:{'goods_id':goods_id},
        datatype:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (msg) {
            if(msg.code == 200){
                $('#num_' + goods_id).text(msg.c_num)
            }else{
                alert(msg.msg)
            }
        },
        error:function (msg) {
            alert('请求失败')
        }
    });
}

function subCart(goods_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/axf/subCart/',
        type:'POST',
        data:{'goods_id':goods_id},
        datatype:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (msg) {
            if(msg.code == 200){
                $('#num_' + goods_id).text(msg.c_num)
            }else{
                alert(msg.msg)
            }
        },
        error:function (msg) {
            alert('请求失败')
        }
    });
}

function changeselect(cart_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'/axf/changeselect/',
        type:'POST',
        data:{'cart_id':cart_id},
        datatype:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            if(data.code == 200){
                if(data.is_select){
                    $('#cart_id_'+cart_id).html('√')
                }else{
                    $('#cart_id_'+cart_id).html('×')
                }
            }
        },
        error:function (data) {
            alert('请求失败')
        }
    });
}

function changeOrderStatus(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    alert(id)
            $.ajax({
                url:'/axf/changeOrderStatus/',
                type: 'POST',
                dataType: 'json',
                data: {'order_id': id},
                headers: {'X-CSRFToken': csrf},
                success: function (msg) {
                    if (msg.code == 200){
                       location.href = '/axf/mine/'
                    }else{
                        alert('支付成功')
                    }
                },
                error: function (msg) {
                    alert('支付失败')
                },

            })
}