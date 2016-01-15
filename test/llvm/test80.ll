; ModuleID = '../src/test80.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test80(i8* %value1) #0 {
  %1 = alloca i8*, align 8
  %local = alloca i32, align 4
  store i8* %value1, i8** %1, align 8
  %2 = load i8** %1, align 8
  %3 = getelementptr inbounds i8* %2, i64 10
  store i8* %3, i8** %1, align 8
  %4 = load i8** %1, align 8
  %5 = load i8* %4, align 1
  %6 = sext i8 %5 to i32
  store i32 %6, i32* %local, align 4
  %7 = load i32* %local, align 4
  ret i32 %7
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
