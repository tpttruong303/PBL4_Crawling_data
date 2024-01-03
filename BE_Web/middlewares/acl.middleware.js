// xử lý các yêu cầu http trước khi chung được xử lý bởi các route
const acl = require('acl');
const aclInstance = new acl(new acl.memoryBackend());
// xác định và quản lý các quy tắc kiểm soát truy cập, kiểm tra xem người dùng hoặc ứng dụng có được phép thực hiện các hành động cụ thể hay không.
// định nghĩa các chứ năng truy cập của admin và user
aclInstance.allow([
	{
		roles: 'admin',
		allows: [
			{ resources: '/users', permissions: '*' },
			{ resources: '/users/:id', permissions: '*' },
			{ resources: '/me', permissions: '*'},
			{ resources: '/', permissions: '*' },

		],
	},
	{
		roles: 'user',
		allows: [
			{ resources: '/me', permissions: ['get', 'post', 'put'] },
			{ resources: '/', permissions: ['get', 'post'] },
			{ resources: '/users/:id', permissions: ['get', 'put'] },
		],
	}
]);

module.exports = aclInstance;