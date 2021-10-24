import discord
from discord.ext import commands
from Database import *

class ToDoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def todo(self, ctx):
        if ctx.invoked_subcommand == None:
            return
    
    @todo.command()
    async def add(self, ctx, index = None, *, task = None):
        if index != None and index.isalpha():
            task = task if task != None else ""
            task = index + f" {task}"
            index = None

        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        elif task == None:
            await ctx.send('No task was entered.')
        else:
            length = len(to_do_list)
            index = length + 1 if index == None else int(index)
            if 0 < index <= length + 1:
                to_do_list.insert(index - 1, task)
                update_to_do_list(name, to_do_list)
                await ctx.send("Task completed.")
            else:
                await ctx.send("Invalid index entered.")
    
    @todo.command()
    async def remove(self, ctx, index = None):
        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        else:
            length = len(to_do_list)
            if index != None and 0 < int(index) <= length:
                index = int(index)
                del to_do_list[index - 1]
                update_to_do_list(name, to_do_list)
                await ctx.send("Task completed.")
            else:
                await ctx.send("Invalid index entered.")
    
    @todo.command()
    async def reorder(self, ctx, index1 = None, index2 = None):
        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        else:
            length = len(to_do_list)
        if index1 != None and 0 < int(index1) <= length and index2 != None and 0 < int(index2) <= length:
            index1, index2 = int(index1), int(index2)
            to_do_list.insert(index2 - 1, to_do_list.pop(index1 - 1))
            update_to_do_list(name, to_do_list)
            await ctx.send("Task completed.")
        else:
            await ctx.send("Invalid index entered.")

    @todo.command()
    async def done(self, ctx, index = None):
        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        else:
            length = len(to_do_list)
            if index != None and 0 < int(index) <= length:
                index = int(index)
                to_do_list[index - 1] = "~~" + to_do_list[index - 1] + "~~"
                update_to_do_list(name, to_do_list)
                await ctx.send("Task completed.")
            else:
                await ctx.send("Invalid index entered.")

    @todo.command()
    async def clear(self, ctx):
        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        else:
            update_to_do_list(name, [])
            await ctx.send("Task completed.")

    @todo.command()
    async def view(self, ctx):
        name = ctx.channel.name
        to_do_list = find_channel_record(name)
        if to_do_list == None:
            await ctx.send("Can't use to-do list functions here!")
        else:
            todo_emb = discord.Embed (
                color = discord.Colour.red(),
                description = "\n".join([f"{count}. {task}" for count, task in enumerate(to_do_list, start = 1)]),
                title = f"To-Do List for Study Group: {name}"
            )

        await ctx.send(embed = todo_emb)

def setup(bot):
    bot.add_cog(ToDoCommands(bot))