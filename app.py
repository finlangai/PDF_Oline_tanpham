from langchain_community.document_loaders import OnlinePDFLoader

loader = OnlinePDFLoader("https://cafef1.mediacdn.vn//Images/Uploaded/DuLieuDownload/BCTC/0002099802371541502cng-ty-c-phn-sa-vit-nam26042024-135808bo-co-ti-chnh-hp-nht-qu-1-nm-2024.pdf")
data = loader.load()
type(data)
print(data[0].page_content)

with open("page_content.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(data[0].page_content)

print("Nội dung của trang đã được lưu vào tệp page_content.txt")
