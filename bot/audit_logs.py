from typing import Optional
from discord import AuditLogAction
from collections import Counter

async def get_logs(guild, action_type: Optional[AuditLogAction] = None, limit=200):
	""" """
	return [
		entry 
		async for entry in guild.audit_logs(limit=limit)
		if action_type is None or entry.action == action_type
	]
