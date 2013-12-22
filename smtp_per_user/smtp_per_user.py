# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class ir_mail_server(osv.osv):
    _inherit = "ir.mail_server"
    _columns = {
        'user_id': fields.many2one('res.users', string="Owner"),
    }

class mail_mail(osv.Model):
    _inherit = "mail.mail"
    def send(self, cr, uid, ids, auto_commit=False, recipient_ids=None, context=None):
        ir_mail_server = self.pool.get('ir.mail_server')
        server_id = ir_mail_server.search(cr, uid, [('user_id', '=', uid)], context=context)
        server_id = server_id and server_id[0] or False
        if server_id:
            self.write(cr, uid, ids, {'mail_server_id': server_id}, context=context)
        return super(mail_mail, self).send(cr, uid, ids, auto_commit=auto_commit, recipient_ids=recipient_ids, context=context)
