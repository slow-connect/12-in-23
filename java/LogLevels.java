public class LogLevels {

    public static String message(String logLine) {
        String[] logLineLst = logLine.split(" ", 2);
        return logLineLst[1].trim();
    }

    public static String logLevel(String logLine) {
        String[] loglevel = logLine.split("]", 2);
        return loglevel[0].substring(1, loglevel[0].length()).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
