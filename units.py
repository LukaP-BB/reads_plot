from statistics import mean
import matplotlib.pyplot as plt
from vizuread import plot_region, get_reads_from, parse_position, READ_SPACING

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(27,10))
# f = "tests/ref.bam"
# plot_region(f, "chr14:105,709,976-105,710,983", ax=ax, piling="compact")
# plt.savefig("test.png")
# # plt.show()

# reads = get_reads_from(f, "chr22:23480074-23483000")
# print([str(r) for r in reads])

f = "/home/luka/Projet/logiciels/transloc_viz/T32126_realigned.fixed.recal.bam"
reads = get_reads_from(f , "chr3:10500-91574691")
n = []
for i, r in enumerate(reads) :
    n.append(r)
    if i > 100 : break

# mean_qual = mean()
plot_region(ax=ax, reads=n)
plt.show()

# position = parse_position("chr22:1-100000000")
# for r in get_reads_from(f, *position) :
#     if "3D" in r.cigar :
#         print(r)
# c1 = "chr11"

# f = "T30989_realigned.fixed.recal.bam"
# c1 = "chr11"
# c2 = "chr14"
# s = "69,638,162"
# e = "69,639,433"

# reads = get_reads_from(f, c1, s, e, flags="-F 2")
# # s = "0"
# # e = "69,639,433"
# # for r in get_reads_from(f, c1, s, e) :
# #     if "3D" in r.cigar :
# #         print(r)

# # reads = get_reads_from(f, *position, samtools_command="samtools")
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,5))

# for i, r in enumerate(reads) :
#     # print(r)
#     r.plot(ax, i)
# plt.show()

# print(is_forward(10))


# cigar = "35H8M1D32M"
# parse_cigar(cigar)