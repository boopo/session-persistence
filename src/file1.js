






/**
 * @api {Get} /daily/df
 * @apiGroup 电费查询
 *
 * @apiParam {String} home 宿舍楼  (梅2楼)
 * @apiParam {String} num  门号    (B4202)
 *
 *
 *@apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/daily/df?home=梅2楼&num=B4202
 *
 *
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回数据
 *
 * @apiError {String}  status  404
 * @apiError {String} msg      抓取失败
 * @apiError {Integer} data 返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
 *
 * {
 *   "status": "200",
 *   "msg": "ok"
 *   "data": "227.43"
 * }
 *@apiErrorExample   {json} Response-Example
 *
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
  }
 *
 */


/**
 * @apiGroup 课表查询
 * @api {Get} /jwxt/kb
 *
 * @apiHeader {String} token 用户授权token
 * @apiParam {String} xnm 年份 如2019
 * @apiParam {String} xqm  学期 如 第一学期：1 第二学期：2
 *
 * @apiParamExample {args} Request-Example
 * http://127.0.0.1:5000/jwxt/kb?xnm=2020&xqm=1
 *
 * @apiSuccess {String} status 200
 * @apiSuccess {String} msg    ok
 * @apiSuccess {string} data   返回列表
 *
 * @apiError {String}  status   404
 * @apiError {String}  msg      抓取失败
 * @apiError {Integer} data    返回数据为null
 *
 * @apiSuccessExample  {json} Response-Example
 * {
 *   "status": 200,
    "msg": "抓取成功",
    "data": {
        "kblx": 7,
        "qsxqj": "1",
        "xqbzxxszList": [],
        "xsxx": {
            "BJMC": "数据科学与大数据技术2019-02班",
            "XNMC": "2019-2020",
            "KXKXXQ": "('3')",
            "XKKGXQ": "1~('3')",
            "XKKG": "1",
            "XH_ID": "08193109",
            "XH": "08193109",
            "XQMMC": "1",
            "XM": "吕迎朝",
            "XQM": "3",
            "XNM": "2019",
            "KCMS": 16
        },
 * }
 *
 * @apiErrorExample   {json} Response-Example
 *
 *{
    "status": 404,
    "msg": "抓取失败",
    "data": "Null"
}
 */





