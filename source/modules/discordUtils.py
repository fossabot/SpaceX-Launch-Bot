"""
Extra things to make the discord library nicer
"""

from discord import errors

from modules.errors import generalErrorEmbed

async def safeSend(client, channel, text=None, embed=None):
    """
    Send a text / embed message (one or the other, not both) to a
    client, and if an error occurs, safely supress it
    On failure, returns:
        -1 : Nothing to send (text & embed are `None`)
        -2 : HTTPException
        -3 : Forbidden
        -4 : InvalidArgument
    On success returns what the client.send_message method returns
    """
    try:
        if text:
            return await client.send_message(channel, text)
        elif embed:
            return await client.send_message(channel, embed=embed)
        else:
            return -1
    except errors.HTTPException:
        return -2  # API down, Message too big, etc.
    except errors.Forbidden:
        return -3  # No permission to message this channel
    except errors.InvalidArgument:
        return -4  # Invalid channel ID (channel deleted)

async def safeSendLaunchInfo(client, channel, embeds):
    """
    Specifically for sending 2 launch embeds, a full-detail one,
    and failing that, a "lite" version of the embed
    
    parameter $embeds:
        Should be as list of 2 embeds, one to attempt to send,
        and one that is garunteed to be under the character
        limit, to send if the first one is too big.
        It could also be a list with just 1 embed, but if this
        is over the char limit, nothing will happen.
        Other errors are automatically handled
    
    Returns 0 if neither embeds are sent
    """
    for embed in embeds:
        v = await safeSend(client, channel, embed=embed)
        if v == -2:
            pass  # Embed might be too big, try lite version
        elif v == -3 or v == -4:
            return 0
        else:
            return v
    # Both failed to send, try to let user know something went wrong
    await safeSend(client, channel, embed=generalErrorEmbed)
    return 0
