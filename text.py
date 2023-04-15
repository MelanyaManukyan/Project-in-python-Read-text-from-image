text = """There. are two different views of how programs differ from projects. In one view, projects deliver outputs, discrete parcels or "chunks" of change;[8] programs create outcomes.[9] In this view, a project might deliver a new factory, hospital or IT system. By combining these projects with other deliverables and changes, their programs might deliver increased income from a new product, shorter waiting lists at the hospital or reduced operating costs due to improved technology. The other view[10] is that a program is nothing more than either a large project or a set (or portfolio) of projects. In this second view, the point of having a program is to exploit economies of scale and to reduce coordination costs and risks. The project manager's job is to ensure that the project succeeds. The program manager, on the other hand, is concerned with the aggregate outcome(s) or end-state result(s) of the collection of projects in a particular program. For example, in a financial institution, a program may include one project that is designed to take advantage of a rising market and another that is designed to protect against the downside of a falling market. The former seeks to leverage the potential upside; the latter to limit the possible downside. A simple analogy is Fix-a-Flat: this highly pressurized aerosol product injects a leak sealant into a punctured tire to stop the outflow of air (project A) and concurrently re-inflates the tire (project B), resulting together in the outcome that a tire that is once again functional (the program comprised projects A and B).According to the view that programs deliver outcomes but projects deliver outputs, program management is concerned with doing the right projects. The program manager has been described as 'playing chess' and keeping the overview in mind, with the pieces to be used or sacrificed being the projects.[12] In contrast, project management is about doing projects right. And also according to this view, successful projects deliver on time, to budget, and to specification, whereas successful programs deliver long-term improvements to an organization. Improvements are usually identified through benefits. An organization should select the group of programs that most take it towards its strategic aims while remaining within its capacity to deliver the changes. On the other hand, the view that programs are simply large projects or a set of projects allows a program may need to deliver tangible benefits quickly.According to one source, the key difference between a program and a project is the finite nature of a project a project must always have a specific end date, else it is an ongoing program.One view of the differences between a program and a project in business is that:A project is unique and is of definite duration. A program is ongoing and implemented within a business to consistently achieve certain results for the business.A project is designed to deliver an output or deliverable and its success will be in terms of delivering the right output at the right time and to the right cost.Program management includes management of projects which, together, improve the performance of the organization. A program's success will be measured in terms of benefits.Benefits are the measures of improvement of an organization and might include increased income, increased profits, decreased costs, improved market position (ability to compete),In the course of achieving required"""

# words = text.split()
# print(text)

# dict_1 = dict()
# sym = ".,;:!"


# for word in words:
#     if word[-1] in sym:
#         subword = word[:-1]
#         dict_1[subword] = 1
#     else:
#         dict_1[word] = 1
# w = {"the": 1}
# print(w.get('bla', 0))


words  = dict()

symbols = " ,.;:!"

# idx = 0
# for i in range(len(text)):
#     if idx == i and text[idx] in symbols:
#         idx += i + 1
#         continue
#     if text[i] in symbols:
#         word = text[idx:i].strip()
#         idx = 1 + i
        
print(words)

text_ls = text.split()
for word in text_ls:
    word = word.strip(symbols)
    words[word] = 1 # top 10 amenashat barery

print(words)