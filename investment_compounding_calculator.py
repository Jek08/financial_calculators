invest_awal = 500000
invest_bulanan = 300000
jangka_waktu = 1
kenaikan_nilai = 12/100
frekuensi_efek_compounding = 12

interest_value = 0
normal_saving = 0
i = 1
while i <= (jangka_waktu * frekuensi_efek_compounding):
    if i is 1:
        interest_value = (invest_awal + (invest_bulanan * (1 + kenaikan_nilai / frekuensi_efek_compounding)))
        normal_saving = invest_awal + invest_bulanan
    elif i is not 1:
        interest_value = ((interest_value + invest_bulanan) * (1 + kenaikan_nilai / frekuensi_efek_compounding))
        normal_saving += invest_bulanan
    print(str(interest_value) + "  #" + str(i))

    i += 1

print("Nilai menabung dengan bunga: Rp " + str(round(interest_value)))
print("Nilai menabung tanpa bunga: Rp " + str(round(normal_saving)))
print("Nilai bunga: Rp " + str(round(interest_value - normal_saving)))