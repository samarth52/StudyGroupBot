import discord
from discord.embeds import Embed
from discord.ext import commands
from Database import *

class StudyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def study(self, ctx):
        if ctx.invoked_subcommand == None:
            return
    
    @study.command()
    async def create(self, ctx):
        checker1 = lambda message: message.author == ctx.author and message.channel == ctx.channel
        checker2 = lambda prompt: lambda reaction, member: reaction.message == prompt and member.name == ctx.author.name

        #Name
        name_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Enter Name of the Study Group:"
        )

        name_prompt = await ctx.send(embed = name_emb)
        name = (await self.bot.wait_for("message", check = checker1)).content
        if name == 'quit':
            return

        #Course
        course_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Course:",
        )

        course_emb.add_field (
            name = "CS 1100",
            value = "0️⃣",
            inline = True
        )
        
        course_emb.add_field (
            name = "CS 1301",
            value = "1️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "CS 1331",
            value = "2️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1551",
            value = "3️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1552",
            value = "4️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1554",
            value = "5️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )   

        course_prompt = await ctx.send(embed = course_emb)
        emojis = {'0️⃣': 'CS 1100', '1️⃣': 'CS 1301', '2️⃣': 'CS 1331', '3️⃣': 'MATH 1551', '4️⃣': 'MATH 1552', '5️⃣': 'MATH 1554',
            '❌': 'quit'}
        for reaction in emojis:
            await course_prompt.add_reaction(reaction)
        course = emojis[(await self.bot.wait_for("reaction_add", check = checker2(course_prompt)))[0].emoji]
        if course:
            await course_prompt.clear_reactions()
        if course == 'quit':
            return

        #East or West
        dir_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Campus Side:",
        )

        dir_emb.add_field (
            name = "West",
            value = "⬅️",
            inline = True
        )

        dir_emb.add_field (
            name = "East",
            value = "➡️",
            inline = True
        )
        
        dir_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )   
    
        east_west_prompt = await ctx.send(embed = dir_emb)
        emojis = {'⬅️': 'West', '➡️': 'East', '❌': 'quit'}
        for reaction in emojis:
            await east_west_prompt.add_reaction(reaction)
        east_west = emojis[(await self.bot.wait_for("reaction_add", check = checker2(east_west_prompt)))[0].emoji]
        if east_west:
            await east_west_prompt.clear_reactions()
        if east_west == 'quit':
            return

        #Location
        if east_west == 'East':
            eastbuild_emb = discord.Embed (
                color = discord.Colour.red(),
                title = "Choose Location to Study in the East:"
            )
            
            eastbuild_emb.add_field (
                name = "Howell Residence Hall",
                value = "0️⃣",
                inline = False
            )

            eastbuild_emb.add_field (
                name = "Brittain Dining Hall",
                value = "1️⃣",
                inline = False
            )

            eastbuild_emb.add_field (
                name = "GT Connector",
                value = "2️⃣",
                inline = False
            )
   
            eastbuild_emb.add_field (
                name = "Quit",
                value = "❌",
                inline = False
            )

            location_prompt = await ctx.send(embed = eastbuild_emb)
            emojis = {'0️⃣': 'Howell Residence Hall', '1️⃣': 'Brittain Dining Hall', '2️⃣': 'GT Connector', '❌': 'quit'}

        elif east_west == 'West':
            westbuild_emb = discord.Embed (
                color = discord.Colour.red(),
                title = "Choose Location to Study in the West:"
            )
          
            westbuild_emb.add_field (
                name = "Fitten Residence Hall",
                value = "0️⃣",
                inline = False
            )

            westbuild_emb.add_field (
                name = "West Village",
                value = "1️⃣",
                inline = False
            )
          
            westbuild_emb.add_field (
                name = "CRC",
                value = "2️⃣",
                inline = False
            )
        
            westbuild_emb.add_field (
                name = "Quit",
                value = "❌",
                inline = False
            )

            location_prompt = await ctx.send(embed = westbuild_emb)
            emojis = {'0️⃣': 'Fitten Residence Hall', '1️⃣': 'West Village', '2️⃣': 'CRC', '❌': 'quit'}

        for reaction in emojis:
            await location_prompt.add_reaction(reaction)
        location = emojis[(await self.bot.wait_for("reaction_add", check = checker2(location_prompt)))[0].emoji]
        if location:
            await location_prompt.clear_reactions()
        if location == 'quit':
            return

        #Now or Later
        now_later_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Scheduling Time:"
        )

        now_later_emb.add_field (
            name = "Now",
            value = "⌛",
            inline = True
        )

        now_later_emb.add_field (
            name = "Later",
            value = "🗓️",
            inline = True
        )

        now_later_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )   

        now_later_prompt = await ctx.send(embed = now_later_emb)
        emojis = {'⌛': 'Now', '🗓️': 'Later', '❌': 'quit'}
        for reaction in emojis:
            await now_later_prompt.add_reaction(reaction)
        now_later = emojis[(await self.bot.wait_for("reaction_add", check = checker2(now_later_prompt)))[0].emoji]
        if now_later:
            await now_later_prompt.clear_reactions()
        if now_later == 'quit':
            return

        #Time
        if now_later == 'Later':
            time_emb = discord.Embed (
                color = discord.Colour.red(),
                title = "Enter Time to Schedule Meeting:"
            )

            time_prompt = await ctx.send(embed = time_emb)
            time = (await self.bot.wait_for("message", check = checker1)).content
            if time == 'quit':
                return
        else:
            time = None

        #Maximum Number of People
        max_number_of_people_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Enter Maximum Number of People:"
        )

        max_number_of_people_prompt = await ctx.send(embed = max_number_of_people_emb)
        max_number_of_people = (await self.bot.wait_for("message", check = checker1)).content
        if max_number_of_people == 'quit':
            return
        max_number_of_people = int(max_number_of_people)

        #channel and db
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages = True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages = True)
        }

        channel = await ctx.guild.create_text_channel(name = name, overwrites = overwrites)

        insert_study_group(name, course, east_west, location, now_later, time, max_number_of_people, [], channel.name)

    @study.command()
    async def display(self, ctx):
        checker1 = lambda message: message.author == ctx.author and message.channel == ctx.channel
        checker2 = lambda prompt: lambda reaction, member: reaction.message == prompt and member.name == ctx.author.name

        #Name
        name_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Enter Name of Study Group (Or 'continue' to skip):"
        )

        name_prompt = await ctx.send(embed = name_emb)
        name = (await self.bot.wait_for("message", check = checker1)).content
        if name == 'quit':
            return
        name = None if name == 'continue' else name

        #Course
        course_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Course:",
        )

        course_emb.add_field (
            name = "CS 1100",
            value = "0️⃣",
            inline = True
        )
        
        course_emb.add_field (
            name = "CS 1301",
            value = "1️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "CS 1331",
            value = "2️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1551",
            value = "3️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1552",
            value = "4️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "MATH 1554",
            value = "5️⃣",
            inline = True
        )

        course_emb.add_field (
            name = "Skip",
            value = "🙅‍♂️",
            inline = True
        )

        course_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )        

        course_prompt = await ctx.send(embed = course_emb)
        emojis = {'0️⃣': 'CS 1100', '1️⃣': 'CS 1301', '2️⃣': 'CS 1331', '3️⃣': 'MATH 1551', '4️⃣': 'MATH 1552', '5️⃣': 'MATH 1554', 
            '🙅‍♂️': None, '❌': 'quit'}
        for reaction in emojis:
            await course_prompt.add_reaction(reaction)
        course = emojis[(await self.bot.wait_for("reaction_add", check = checker2(course_prompt)))[0].emoji]
        if course or course is None:
            await course_prompt.clear_reactions()
        if course == 'quit':
            return

        #East or West
        dir_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Campus Side:",
        )

        dir_emb.add_field (
            name = "West",
            value = "⬅️",
            inline = True
        )

        dir_emb.add_field (
            name = "East",
            value = "➡️",
            inline = True
        )

        dir_emb.add_field (
            name = "Skip",
            value = "🙅‍♂️",
            inline = True
        )

        dir_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )   
        
        east_west_prompt = await ctx.send(embed = dir_emb)
        emojis = {'➡️': 'East', '⬅️': 'West', '🙅‍♂️': None, '❌': 'quit'}
        for reaction in emojis:
            await east_west_prompt.add_reaction(reaction) #Need to check he doesn't use any other emoji
        east_west = emojis[(await self.bot.wait_for("reaction_add", check = checker2(east_west_prompt)))[0].emoji]
        if east_west or east_west is None:
            await east_west_prompt.clear_reactions()
        if east_west == 'quit':
            return
        
        #Location
        if east_west is not None:
            if east_west == 'East':
                eastbuild_emb = discord.Embed (
                    color = discord.Colour.red(),
                    title = "Choose Location to Study in the East:"
                )
                
                eastbuild_emb.add_field (
                    name = "Howell Residence Hall",
                    value = "0️⃣",
                    inline = True
                )

                eastbuild_emb.add_field (
                    name = "Brittain Dining Hall",
                    value = "1️⃣",
                    inline = True
                )

                eastbuild_emb.add_field (
                    name = "GT Connector",
                    value = "2️⃣",
                    inline = True
                )

                eastbuild_emb.add_field (
                    name = "Skip",
                    value = "🙅‍♂️",
                    inline = True
                )

                eastbuild_emb.add_field (
                    name = "Quit",
                    value = "❌",
                    inline = True
                )   
                
                location_prompt = await ctx.send(embed = eastbuild_emb)
                emojis = {'0️⃣': 'Howell Residence Hall', '1️⃣': 'Brittain Dining Hall', '2️⃣': 'GT Connector', '🙅‍♂️': None,
                    '❌': 'quit'}

            elif east_west == 'West':
                westbuild_emb = discord.Embed (
                    color = discord.Colour.red(),
                    title = "Choose Location to Study in the West:"
                )
            
                westbuild_emb.add_field (
                    name = "Fitten Residence Hall",
                    value = "0️⃣",
                    inline = True
                )

                westbuild_emb.add_field (
                    name = "West Village",
                    value = "1️⃣",
                    inline = True
                )
            
                westbuild_emb.add_field (
                    name = "CRC",
                    value = "2️⃣",
                    inline = True
                )

                westbuild_emb.add_field (
                    name = "Skip",
                    value = "🙅‍♂️",
                    inline = True
                )

                westbuild_emb.add_field (
                    name = "Quit",
                    value = "❌",
                    inline = True
                )   

                location_prompt = await ctx.send(embed = westbuild_emb)
                emojis = {'0️⃣': 'Fitten Residence Hall', '1️⃣': 'West Village', '2️⃣': 'CRC', '🙅‍♂️': None, '❌': 'quit'}
            for reaction in emojis:
                await location_prompt.add_reaction(reaction) #Need to check he doesn't use any other emoji
            location = emojis[(await self.bot.wait_for("reaction_add", check = checker2(location_prompt)))[0].emoji]
            if location or location is None:
                await location_prompt.clear_reactions()
            if location == 'quit':
                return
        else:
            location = None

        #Now or Later
        now_later_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Choose Scheduling Time:"
        )

        now_later_emb.add_field (
            name = "Now",
            value = "⌛",
            inline = True
        )

        now_later_emb.add_field (
            name = "Later",
            value = "🗓️",
            inline = True
        )

        now_later_emb.add_field (
            name = "Skip",
            value = "🙅‍♂️",
            inline = True
        )

        now_later_emb.add_field (
            name = "Quit",
            value = "❌",
            inline = True
        )   
        
        now_later_prompt = await ctx.send(embed = now_later_emb)
        emojis = {'⌛': 'Now', '🗓️': 'Later', '🙅‍♂️': None, '❌': 'quit'}
        for reaction in emojis:
            await now_later_prompt.add_reaction(reaction) #Need to check he doesn't use any other emoji
        now_later = emojis[(await self.bot.wait_for("reaction_add", check = checker2(now_later_prompt)))[0].emoji]
        if now_later or now_later is None:
            await now_later_prompt.clear_reactions()
        if now_later == 'quit':
            return

        #Time
        if now_later == 'Later':
            time_emb = discord.Embed (
                color = discord.Colour.red(),
                title = "Enter Time to Schedule Meeting (Or 'continue' to skip):"
            )

            time_prompt = await ctx.send(embed = time_emb)
            time = (await self.bot.wait_for("message", check = checker1)).content
            time = None if time == 'continue' else time
            if time == 'quit':
                return
        else:
            time = None

        #Maximum Number of People
        max_number_of_people_emb = discord.Embed (
            color = discord.Colour.red(),
            title = "Enter Maximum Number of People (Or 'continue' to skip):"
        )

        max_number_of_people_prompt = await ctx.send(embed = max_number_of_people_emb)
        max_number_of_people = (await self.bot.wait_for("message", check = checker1)).content
        if max_number_of_people == 'quit':
            return
        max_number_of_people = None if max_number_of_people == 'continue' else int(max_number_of_people)

        results = match_study_group(name, course, east_west, location, now_later, time, max_number_of_people)
        for result in results:
            await embed_study_group(ctx, result)

async def embed_study_group(ctx, study_group):
    study_sessions_emb = discord.Embed (
        color = discord.Colour.red(),
        title = "Study Sessions for You",
    )

    study_sessions_emb.add_field (
        name = "Name:",
        value = study_group['name'],
        inline = True
    )

    study_sessions_emb.add_field (
        name = "Course:",
        value = study_group['course'],
        inline = True
    )

    study_sessions_emb.add_field (
        name = "Location:",
        value = study_group['location'],
        inline = True
    )
    
    to_output = "Now" if study_group['now_later'] == 'Now' else study_group['time']

    study_sessions_emb.add_field (
        name = "Meeting Time:", 
        value = to_output,
        inline = True
    )

    study_sessions_emb.add_field (
        name = "Number of Participants:", 
        value = f"{study_group['current_number_of_people']} / {study_group['max_number_of_people']}",
        inline = True
    )

    await ctx.send(embed = study_sessions_emb)


def setup(bot):
    bot.add_cog(StudyCommands(bot))
