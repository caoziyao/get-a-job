// 定义一个空对象
// 这个对象用来和服务器通信
// 这样我们只需使用函数而不用关心服务器的具体细节
var api = {}

var log = function(){
    console.log(arguments)
}

/*
给对象添加一个 ajax 方法
它接受 url method form 等 4 个参数
其中 callback 是函数，用于在收到服务器响应后回调
*/
api.ajax = function(url, method, form, callback){
    // 生成一个请求
    var request = {
        url: url,
        type: method,
        data: form,
        success: function(response){
            log('sucess')
            // 这个 response 是 ajax 给我们传的参数
            // 解析后 调用 callback 函数并把参数传给他
            // var r = JSON.parse(response)
            callback(r)
        },
        error: function(err){
            log('err')
            var r = {
                'success': false,
                message: '网络错误'
            }
            callback(r)
        }
    }

    // 用 jQuery 的 ajax 函数发送这个请求
    log('api ajax')
    $.ajax(request)
}

/*
api 内部函数，发一个 post 请求
*/
api.post = function(url, form, response) {
    // response 是一个回调函数
    api.ajax(url, 'post', form, response)
}

api.get = function(url, response) {
    // response 是一个回调函数
    form = {}
    api.ajax(url, 'get', form, response)
}

///////////api////////////////////
