"""Password Reset Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_verify_identity():
    """Test Verify user identity through security questions or MFA."""
    tools = AgentTools()
    result = await tools.verify_identity(user_id="test", verification_method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_reset_password():
    """Test Reset password in the target system after identity verification."""
    tools = AgentTools()
    result = await tools.reset_password(user_id="test", target_system="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_password_policy():
    """Test Validate a new password against organizational policy."""
    tools = AgentTools()
    result = await tools.check_password_policy(password="test", user_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_unlock_account():
    """Test Unlock a locked account after too many failed attempts."""
    tools = AgentTools()
    result = await tools.unlock_account(user_id="test", target_system="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.password_reset_agent_agent import PasswordResetAgentAgent
    agent = PasswordResetAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
