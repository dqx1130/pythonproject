复制代码
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.multipart.MultipartFile;

import com.cetcbigdata.common.CetcBigDataException;
import com.cetcbigdata.enums.ErrorCode;
import com.cetcbigdata.enums.FileType;
import com.cetcbigdata.enums.UploadFileType;

/**
 * @author
 * @version 创建时间：2019年4月9日 上午9:49:58
 *
 *
 *          文件类型判断类型 注意：txt文档没有文件头，无法通过该方法判断文件类型
 */
public final class FileTypeJudge {
    private final static Logger logger = LoggerFactory.getLogger(FileTypeJudge.class);

    //定义文件分类，可以自定义其他文件分类
    public  final static  FileType[] pics = { FileType.JPEG, FileType.PNG, FileType.GIF, FileType.TIFF, FileType.BMP, FileType.DWG,
            FileType.PSD };

    public  final static FileType[] docs = { FileType.RTF, FileType.XML, FileType.XLS_DOC, FileType.XLSX_DOCX, FileType.WPS, FileType.WPD,
            FileType.PDF, FileType.ZIP, FileType.RAR, FileType.MF, FileType.CHM };

    public  final static FileType[] audios = { FileType.WAV, FileType.MP3 };

    public  final static FileType[] videos = { FileType.AVI, FileType.RAM, FileType.RM, FileType.MPG, FileType.MOV, FileType.ASF,
            FileType.MP4, FileType.FLV, FileType.MID };

    private FileTypeJudge() {
        super();
    }

    /**
     * 将文件头转换成16进制字符串
     *
     * @param 原生byte
     * @return 16进制字符串
     */
    private static String bytesToHexString(byte[] src) {

        StringBuilder stringBuilder = new StringBuilder();
        if (src == null || src.length <= 0) {
            return null;
        }
        for (int i = 0; i < src.length; i++) {
            int v = src[i] & 0xFF;
            String hv = Integer.toHexString(v);
            if (hv.length() < 2) {
                stringBuilder.append(0);
            }
            stringBuilder.append(hv);
        }
        return stringBuilder.toString();
    }

    /**
     * 得到文件头
     *
     * @param inputStream 文件流
     * @return 文件头
     * @throws IOException
     */
    private static String getFileContent(InputStream is) throws IOException {
        byte[] b = new byte[28];
        try {
            is.read(b, 0, 28);
        } catch (IOException e) {
            logger.error("---读取文件头失败：{}-----", e.getMessage());
            throw e;
        }
        return bytesToHexString(b);
    }

    /**
     * 判断文件类型
     *
     * @param inputStream 文件流
     * @return 文件类型
     */
    public static FileType getType(InputStream inputStream) throws IOException {
        if (inputStream == null) {
            throw new CetcBigDataException(ErrorCode.PARAMETER_ERROR.getCode(), ErrorCode.PARAMETER_ERROR.getMsg());
        }
        String fileHead = getFileContent(inputStream);
        if (fileHead == null || fileHead.length() == 0) {
            return null;
        }
        fileHead = fileHead.toUpperCase();
        FileType[] fileTypes = FileType.values();

        for (FileType type : fileTypes) {
            if (fileHead.startsWith(type.getValue())) {
                return type;
            }
        }
        return null;
    }

    /**
     *
     * @param value 表示文件类型
     * @return UploadFileType
     * @return
     */
    public static UploadFileType getUploadFileType(FileType value) {
        if (value == null) {
            return null;
        }
        // 图片
        for (FileType fileType : pics) {
            if (fileType.equals(value)) {
                return UploadFileType.IMG;
            }
        }
        // 文档
        for (FileType fileType : docs) {
            if (fileType.equals(value)) {
                return UploadFileType.DOC;
            }
        }
        // 音乐
        for (FileType fileType : audios) {
            if (fileType.equals(value)) {
                return UploadFileType.AUDIO;
            }
        }
        // 视频
        for (FileType fileType : videos) {
            if (fileType.equals(value)) {
                return UploadFileType.VIDEO;
            }
        }
        return UploadFileType.OTHER;
    }

    /***
     *
     * @param file
     * @return
     * @throws FileNotFoundException
     * @throws IOException
     */
    public static UploadFileType getUploadFileType(File file) throws FileNotFoundException, IOException {
        if (file == null || file.length() <= 0) {
            throw new CetcBigDataException(ErrorCode.PARAMETER_ERROR.getCode(), ErrorCode.PARAMETER_ERROR.getMsg());
        }
        FileType fileType = getType(new FileInputStream(file));

        return getUploadFileType(fileType);
    }

    /***
     * 上传文件可以直接调用该方法判断文件大类
     *
     * @param multipartFile
     * @return
     * @throws FileNotFoundException
     * @throws IOException
     */
    public static UploadFileType getUploadFileType(MultipartFile multipartFile)
            throws FileNotFoundException, IOException {
        if (multipartFile == null || multipartFile.getSize() <= 0) {
            throw new CetcBigDataException(ErrorCode.PARAMETER_ERROR.getCode(), ErrorCode.PARAMETER_ERROR.getMsg());
        }
        FileType fileType = getType(multipartFile.getInputStream());

        return getUploadFileType(fileType);
    }

    public static void main(String args[]) throws Exception {
        File file = new File("E:\\爬虫应用工作总结.pptx");
        System.out.println(file.length());
        System.out.println(FileTypeJudge.getUploadFileType(file));

    }

}
