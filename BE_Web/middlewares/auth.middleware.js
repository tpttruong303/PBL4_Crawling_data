const jwt = require('jsonwebtoken');
require('dotenv').config()
const acl = require('./acl.middleware');
const authorize = (req, res, next) => { // Hàm này sẽ được gọi để kiểm tra quyền truy cập trước khi xử lý các yêu cầu HTTP.
	if (!req.headers.authorization) {
		return res.status(401).json({ message: 'Unauthorized1' });
	} else {
		try {
			const token = req.headers.authorization.split(' ').length == 2 ? req.headers.authorization.split(' ')[1] : req.headers.authorization; //trích xuất token
			const decoded = jwt.verify(token, process.env.SECRET); //giải mã token jwt
			console.log("checktoken:",token,"checkSecretKey:",process.env.SECRET)
			const userRole = decoded.role;
			console.log(userRole);
			acl.areAnyRolesAllowed(userRole, req.route.path, req.method.toLowerCase(), (err, result) => { // kiểm tra xem vai trò người dùng có truy cập đến đường dẫn hay không
				if (err) {
					console.log(err);
				} else {
					if (result) {
						next(); 
					} else {
						return res.status(401).json({ message: 'Forbidden' });
					}
				}
			})
		} catch (error) {
			console.log(error);
			return res.status(401).json({ message: 'Unauthorized2' });
		}
	}
};
module.exports = {authorize};